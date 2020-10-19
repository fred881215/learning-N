// const socket = io.connect('http://' + eth0IP + ':9806');
// const socket = io.connect('http://10.21.20.52:9806');
// const socket = io.connect('http://127.0.0.1:3000');

let msgloop = false;
let beforedata = '';
let count = 0;

function publishReturn(active) {
    console.log('publishReturn');
    console.log(active);
    if (active == 'create' || active == 'exist' || active == 'kill' || active == 'not create') {
        //send message from b to a
        let ul_A = document.getElementById("listA");
        let li_A = document.createElement("li");
        li_A.innerHTML = "<div class = 'message-b-to-a-sty' ><img src='/static/img/opendds.png' alt='B' class='message-img' width='31px' class='message-img' height='31px'><div>" + new Date().toLocaleString() + ' publish狀態：' + active + "</div></div>"
        ul_A.appendChild(li_A);
        ul_A.scrollTop = ul_A.scrollHeight;
    } else {
        try {
            //send message from a to a
            let ul_A = document.getElementById("listA");
            let li_A = document.createElement("li");
            li_A.innerHTML = "<div class = 'message-a-to-a-sty' ><div>" + new Date().toLocaleString() + active + "</div></div>";
            ul_A.appendChild(li_A);
            ul_A.scrollTop = ul_A.scrollHeight;
            msgID = "";
        } catch (e) {
            console.log('json error');
        }
    }
};
function subscriberRecevie(active) {
    console.log('subscriberRecevie');
    console.log(active);
    if (active == 'create' || active == 'start subscriber recevie' || active == 'not create' || active == 'exist' || active == 'kill') {
        if (active == 'start subscriber recevie'){
            msgloop = true;
        }
        if(active == 'kill'){
            msgloop = false;
        }
        //send message from b to a
        let ul_A = document.getElementById("listA");
        let li_A = document.createElement("li");
        li_A.innerHTML = "<div class = 'message-b-to-a-sty' ><img src='/static/img/opendds.png' alt='B' class='message-img' width='31px' height='31px'><div>" + new Date().toLocaleString() + ' subscriber狀態：' + active + "</div></div>"
        ul_A.appendChild(li_A);
        ul_A.scrollTop = ul_A.scrollHeight;
    } else {
        //send message from b to a
        let ul_A = document.getElementById("listA");
        let li_A = document.createElement("li");
        li_A.innerHTML = "<div class = 'message-b-to-a-sty' ><img src='/static/img/opendds.png' alt='B' class='message-img' width='31px' height='31px'><div>" + new Date().toLocaleString() + ' subscriber接收到的資料：' + active + "</div></div>"
        ul_A.appendChild(li_A);
        ul_A.scrollTop = ul_A.scrollHeight;
    }
};
setInterval(function () {
    if (msgloop) {
        subloop()
    }
}, 3000);
function subloop(active) {
    axios.get('/subloop')
    .then(function (data) {
        msgcount = parseInt(data.data.msgcount,10);
        if (msgcount != count) {
            subscriberRecevie(data.data.data);
            count += 1;
        }
        beforedata = data.data.data;
    })
    .catch(function (error) {
        console.log('error');
    })
};
var app = new Vue({
    el:'#main',
    methods: {
        sendA: function() {
            msgID = parseInt(Math.random() * Math.pow(10, 16)).toString();
            msg_text = this.$refs.msgA.value;
            let message = {"from": msgID, "message": msg_text, "topic": {"eth0IP":eth0IP, "eth0NetMask":eth0NetMask, "eth0gateway":eth0gateway, "eth0dns":eth0dns}};
            axios.post('/sendmsgA', message)
            .then(function (data) {
                console.log('success');
                publishReturn(message.message);
            })
            .catch(function (error) {
                console.log('error');
                publishReturn('發送失敗');
            });
            msgA.value = "";
        },
        publishCreate: function() {
            ini = this.$refs.publishIni.value;
            let pubSettingSave = { "type": "pub", "topic": {"eth0IP":eth0IP, "eth0NetMask":eth0NetMask, "eth0gateway":eth0gateway, "eth0dns":eth0dns}, "rtps": ini}
            console.log(pubSettingSave);
            axios.post('/pubSetting', pubSettingSave)
            .then(function (data) {
                console.log('success');
                publishReturn("create");
            })
            .catch(function (error) {
                console.log('error');
            });
        },
        publishStatus: function() {
            let action = {"active": "status"}
            axios.post('/pubSetting', action)
            .then(function (data) {
                console.log('success');
                var data = JSON.parse(JSON.stringify(data));
                console.log(data.data.status);
                publishReturn(data.data.status);
                }
            )
            .catch(function (error) {
                console.log('error');
            });
        },
        publishExit: function() {
            let action = {"active": "exit"}
            axios.post('/pubSetting', action)
            .then(function (data) {
                console.log('success');
                publishReturn("not create");
            })
            .catch(function (error) {
                console.log('error');
            });
        },
        publishKill: function() {
            let action = {"active": "kill"}
            axios.post('/pubSetting', action)
            .then(function (data) {
                console.log('success');
                publishReturn("kill");
            })
            .catch(function (error) {
                console.log('error');
            });
        },
        subscriberCreate: function() {
            ini = this.$refs.subscriberIni.value;
            topic_eth0IP = this.$refs.subscriberTopic_eth0IP.value;
            topic_eth0NetMask = this.$refs.subscriberTopic_eth0NetMask.value;
            topic_eth0gateway = this.$refs.subscriberTopic_eth0gateway.value;
            topic_eth0dns = this.$refs.subscriberTopic_eth0dns.value;
            let subSettingSave = { "type": "sub", "topic": {"eth0IP":topic_eth0IP, "eth0NetMask":topic_eth0NetMask, "eth0gateway":topic_eth0gateway, "eth0dns":topic_eth0dns}, "rtps": ini}
            axios.post('/subSetting', subSettingSave)
            .then(function (data) {
                console.log('success');
                subscriberRecevie("create");
            })
            .catch(function (error) {
                console.log('error');
            });
            subscriberTopic_eth0IP.value = "";
            subscriberTopic_eth0NetMask.value = "";
            subscriberTopic_eth0gateway.value = "";
            subscriberTopic_eth0dns.value = "";
        },
        subscriberStart: function() {
            let action = {"active": "start"}
            axios.post('/subSetting', action)
            .then(function (data) {
                console.log('success');
                console.log(data.data.status);
                subscriberRecevie("start subscriber recevie");
            })
            .catch(function (error) {
                console.log('error');
            });
        },
        subscriberStatus: function() {
            let action = {"active": "status"}
            axios.post('/subSetting', action)
            .then(function (data) {
                console.log('success');
                var data = JSON.parse(JSON.stringify(data));
                console.log(data.data.status);
                publishReturn(data.data.status);
            })
            .catch(function (error) {
                console.log('error');
            });
        },
        subscriberKill: function() {
            let action = {"active": "kill"}
            axios.post('/subSetting', action)
            .then(function (data) {
                console.log('success');
                subscriberRecevie("kill");
            })
            .catch(function (error) {
                console.log('error');
            });
        },
    },
});
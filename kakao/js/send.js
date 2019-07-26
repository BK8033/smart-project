const { config, Group } = require('solapi')
const conf = require('../config')

/*
 solapi js example
 send simple messages
*/

config.init({
  apiKey: conf.apiKey,
  apiSecret: conf.apiSecret
})
send({
  text: 'java tet',
  type: conf.type,
  to: '01053658033',
  from: '01053658033'
})
async function send (message, agent = {}) {
  try {
    console.log(await Group.sendSimpleMessage(message, agent))
  } catch (e) {
    console.log(e)
  }
}

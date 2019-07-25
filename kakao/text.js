const { config, Group } = require('coolsms-sdk-v4')

// 인증을 위해 발급받은 본인의 API Key를 사용합니다.
const apiKey = 'NCS3CFAYW7TVC6EP'
const apiSecret = '374ICW9HWOUNT0CBB23KTMXF0EFAHSB4'
config.init({ apiKey, apiSecret })
async function send (params = {}) {
      try {
              const response = await Group.sendSimpleMessage(params)
                  console.log(response)
                    } catch (e) {
                            console.log(e)
                              }
}

const params = {
      text: '[솔라피 테스트] hello world!', // 문자 내용
        type: 'SMS', // 발송할 메시지 타입 (SMS, LMS, MMS, ATA, CTA)
          to: '01053658033', // 수신번호 (받는이)
            from: '01053658033' // 발신번호 (보내는이)
}
send(params)

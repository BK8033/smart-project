module.exports = {
// 계정의 ApiKey와 ApiSecret을 입력해주세요
// https://solapi.com/credentials
  apiKey: 'NCS3CFAYW7TVC6EP',
  apiSecret: '374ICW9HWOUNT0CBB23KTMXF0EFAHSB4',
  type: 'SMS', // 문자 타입 (SMS, LMS, MMS, CTA, ATA)
  to: '01053658033', // 문자를 받을 수신번호
  from: '01000000000', // https://solapi.com/senderids 에서 등록한 발신번호
  text: '' // 문자 내용
}

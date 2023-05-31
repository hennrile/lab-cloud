const express = require('express')
const app = express()
const router = express.Router()

function handleRequest(req, res) {
  const deviceType = req.get('User-Agent')
  let responseMsg = ''

  if (deviceType.includes('Mobile')) {
    responseMsg = 'Hello from mobile device!'
  } else if (deviceType.includes('Tablet')) {
    responseMsg = 'Hello from tablet device!'
  } else {
    responseMsg = 'Hello from desktop device!'
  }

  res.send(responseMsg)
}

router.get('/', handleRequest)

app.use('/', router)

const PORT = process.env.PORT || 3000

app.listen(PORT, () => {
  console.log(`Web server is listening on port ${PORT}`)
})
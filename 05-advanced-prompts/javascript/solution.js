// starter code
const express = require('express')

const app = express()

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(3000, () => {
  console.log('Example app listening on port 3000!')
})


// prompt in Copilot Chat, find 3 improvements to the code and apply
// results:

/*
Sure, here are three improvements that can be made to the code:

1. The warning "File is a CommonJS module; it may be converted to an ES module" can be resolved by adding "type": "module" to the package.json file. This will allow the use of ES modules in the project.

1. The warning "'req' is declared but its value is never read" can be resolved by removing the req parameter from the callback function of the app.get() method. Since the req parameter is not used in the function, it can be safely removed.

1. The console.log() statement in the app.listen() method can be replaced with a more descriptive message. For example, "Server is running on port 3000" would be a more informative message.

Here is the updated code with the suggested improvements:
*/
import express from 'express';

const app = express();

app.get('/', (_, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});

// Prompt: improve the code and make it more secure

/* 
Sure, here are some suggestions to improve the code and make it more secure:

1. Use environment variables to store sensitive information such as database credentials, API keys, and other secrets. This will prevent the information from being hard-coded in the code and exposed in case of a security breach.

1. Implement input validation to prevent malicious input from being processed by the server. For example, you can use a library like express-validator to validate user input and sanitize it before processing.

1. Use HTTPS instead of HTTP to encrypt data in transit and prevent eavesdropping and man-in-the-middle attacks. You can use a library like https to create an HTTPS server and obtain a TLS/SSL certificate from a trusted certificate authority.

Here is the updated code with the suggested improvements:
*/
import express from 'express';
import https from 'https';
import fs from 'fs';
import { check, validationResult } from 'express-validator';

const app = express();

// Use environment variables to store sensitive information
const PORT = process.env.PORT || 3000;
const DB_USER = process.env.DB_USER;
const DB_PASS = process.env.DB_PASS;

// Implement input validation
app.get('/', [
  check('name').isLength({ min: 3 }).withMessage('Name must be at least 3 characters'),
  check('email').isEmail().withMessage('Invalid email address'),
], (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  const { name, email } = req.query;
  res.send(`Hello ${name} (${email})!`);
});

// Use HTTPS instead of HTTP
const options = {
  key: fs.readFileSync('server.key'),
  cert: fs.readFileSync('server.cert')
};

https.createServer(options, app).listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

/*
Note that the server.key and server.cert files are required to create an HTTPS server. You can generate a self-signed certificate using the following command:
*/

```bash
openssl req -nodes -new -x509 -keyout server.key -out server.cert
```

/* 
This will generate a `server.key` and `server.cert` file in the current directory. However, for production use, you should obtain a TLS/SSL certificate from a trusted certificate authority.
*/





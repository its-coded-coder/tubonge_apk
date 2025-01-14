
### Documentation for "Tubonge" Project Setup

#### Frontend Setup

1. **Create a new React Native Expo project:**
    - Open a terminal and run the following commands to create a new React Native Expo project:
    ```bash
    npx create-expo-app tubonge_app
    cd tubonge_app
    npm install
    ```

2. **Integrate Firebase for user authentication:**
    - Install Firebase SDK:
    ```bash
    npm install @react-native-firebase/app @react-native-firebase/auth
    ```
    - Initialize Firebase in your project:
    ```javascript
    // firebaseConfig.js
    import { initializeApp } from 'firebase/app';
    import { getAuth } from 'firebase/auth';

    const firebaseConfig = {
      apiKey: "YOUR_API_KEY",
      authDomain: "YOUR_AUTH_DOMAIN",
      projectId: "YOUR_PROJECT_ID",
      storageBucket: "YOUR_STORAGE_BUCKET",
      messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
      appId: "YOUR_APP_ID"
    };

    const app = initializeApp(firebaseConfig);
    const auth = getAuth(app);

    export { auth };
    ```
    - Implement user registration and login screens:
    ```javascript
    // screens/RegisterScreen.js
    import React, { useState } from 'react';
    import { View, TextInput, Button, Text } from 'react-native';
    import { auth } from '../firebaseConfig';
    import { createUserWithEmailAndPassword } from 'firebase/auth';

    const RegisterScreen = () => {
      const [email, setEmail] = useState('');
      const [password, setPassword] = useState('');
      const [error, setError] = useState('');

      const handleRegister = async () => {
        try {
          await createUserWithEmailAndPassword(auth, email, password);
        } catch (err) {
          setError(err.message);
        }
      };

      return (
        <View>
          <TextInput
            placeholder="Email"
            value={email}
            onChangeText={setEmail}
          />
          <TextInput
            placeholder="Password"
            value={password}
            onChangeText={setPassword}
            secureTextEntry
          />
          <Button title="Register" onPress={handleRegister} />
          {error ? <Text>{error}</Text> : null}
        </View>
      );
    };

    export default RegisterScreen;
    ```

    ```javascript
    // screens/LoginScreen.js
    import React, { useState } from 'react';
    import { View, TextInput, Button, Text } from 'react-native';
    import { auth } from '../firebaseConfig';
    import { signInWithEmailAndPassword } from 'firebase/auth';

    const LoginScreen = () => {
      const [email, setEmail] = useState('');
      const [password, setPassword] = useState('');
      const [error, setError] = useState('');

      const handleLogin = async () => {
        try {
          await signInWithEmailAndPassword(auth, email, password);
        } catch (err) {
          setError(err.message);
        }
      };

      return (
        <View>
          <TextInput
            placeholder="Email"
            value={email}
            onChangeText={setEmail}
          />
          <TextInput
            placeholder="Password"
            value={password}
            onChangeText={setPassword}
            secureTextEntry
          />
          <Button title="Login" onPress={handleLogin} />
          {error ? <Text>{error}</Text> : null}
        </View>
      );
    };

    export default LoginScreen;
    ```

3. **Setup Navigation:**
    - Install React Navigation:
    ```bash
    npm install @react-navigation/native @react-navigation/stack
    npm install react-native-screens react-native-safe-area-context
    ```
    - Configure navigation in your project:
    ```javascript
    // App.js
    import React from 'react';
    import { NavigationContainer } from '@react-navigation/native';
    import { createStackNavigator } from '@react-navigation/stack';
    import RegisterScreen from './screens/RegisterScreen';
    import LoginScreen from './screens/LoginScreen';

    const Stack = createStackNavigator();

    const App = () => {
      return (
        <NavigationContainer>
          <Stack.Navigator initialRouteName="Login">
            <Stack.Screen name="Register" component={RegisterScreen} />
            <Stack.Screen name="Login" component={LoginScreen} />
          </Stack.Navigator>
        </NavigationContainer>
      );
    };

    export default App;
    ```

#### Backend Setup

1. **Create a new Node.js project:**
    - Open a terminal and run the following commands to create a new Node.js project:
    ```bash
    mkdir tubonge_backend
    cd tubonge_backend
    npm init -y
    ```

2. **Install Express and Firebase Admin SDK:**
    - Install the required packages:
    ```bash
    npm install express firebase-admin
    ```
    - Initialize Firebase Admin SDK in your project:
    ```javascript
    // firebaseAdmin.js
    const admin = require('firebase-admin');
    const serviceAccount = require('./path/to/serviceAccountKey.json');

    admin.initializeApp({
      credential: admin.credential.cert(serviceAccount),
      databaseURL: 'https://YOUR_PROJECT_ID.firebaseio.com'
    });

    module.exports = admin;
    ```

3. **Create Express server:**
    - Create a basic Express server:
    ```javascript
    // server.js
    const express = require('express');
    const admin = require('./firebaseAdmin');

    const app = express();
    const port = process.env.PORT || 3000;

    app.use(express.json());

    app.post('/register', async (req, res) => {
      const { email, password } = req.body;
      try {
        const user = await admin.auth().createUser({
          email,
          password,
        });
        res.status(201).send(user);
      } catch (error) {
        res.status(400).send(error.message);
      }
    });

    app.post('/login', async (req, res) => {
      const { email, password } = req.body;
      try {
        const user = await admin.auth().getUserByEmail(email);
        // Implement your own password verification logic here
        res.status(200).send(user);
      } catch (error) {
        res.status(400).send(error.message);
      }
    });

    app.listen(port, () => {
      console.log(`Server is running on port ${port}`);
    });
    ```

#### Deployment

1. **Deploy the frontend to Expo:**
    - Run the following command to publish your Expo project:
    ```bash
    expo publish
    ```

2. **Deploy the backend to Heroku:**
    - Create a new Heroku app and push your code:
    ```bash
    heroku create tubonge-backend
    git push heroku main
    ```

3. **Configure environment variables:**
    - Set the required environment variables in Heroku:
    ```bash
    heroku config:set FIREBASE_SERVICE_ACCOUNT_KEY="$(cat path/to/serviceAccountKey.json)"
    ```

4. **Monitor and manage your deployments:**
    - Use the Heroku dashboard to monitor and manage your backend deployment.
    - Use the Expo dashboard to monitor and manage your frontend deployment.

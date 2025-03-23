import Login from './components/Login';
import Register from './components/Register';
import { useState } from 'react';

function App() {
  const [showRegister, setShowRegister] = useState(false);

  return (
    <div className="App">
      <button onClick={() => setShowRegister(!showRegister)}>
        {showRegister ? 'Go to Login' : 'Go to Register'}
      </button>
      {showRegister ? <Register /> : <Login />}
    </div>
  );
}

export default App;
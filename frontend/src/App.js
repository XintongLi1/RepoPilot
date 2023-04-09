import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import { DisplayArea } from './components/displayArea'
const BACKEND_URL = 'http://127.0.0.1:3001'




function App() {
  const [displayData, setDisplayData] = useState('');
  const [displayDataType, setDisplayDataType] = useState(false);

  async function getSummary() {
    setDisplayDataType('summary')
    setDisplayData(await (await fetch(BACKEND_URL + '/summary')).json());
  }

  async function getRankings() {
    
    setDisplayData((await (await fetch(BACKEND_URL + '/rank_all')).json()));
    setDisplayDataType('rank_all')
  }

  return (
    <div className="App">
      <header className="App-header">

        <button onClick={getSummary}>Summary</button>
        <button onClick={getRankings}>getRankings</button>
        
          <DisplayArea type={displayDataType} data={displayData}></DisplayArea>
        


      </header>
    </div>
  );
}

export default App;

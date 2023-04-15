import './App.css';
import ProgressBar from 'react-bootstrap/ProgressBar';
import Timer from './components/Timer.jsx'
import Status from './components/Status.jsx'
import Line from './components/Line.jsx'
import BasicExample from './components/Line.jsx';

function App() {
  return (
    <div className="App">
      <div className="first-column">
        <Status name="COMMISIONING" status="Normal"></Status>
        <Status name="ON PAD" status="Normal"></Status>
        <Status name="MOTOR 1 BURN" status="Abort"></Status>
        <Status name="COAST 1" status="Normal"></Status>
        <Status name="MOTOR 2 IGNITION" status="Abort"></Status>
        <Status name="MOTOR 2 BURN" status="Abort"></Status>
        <Status name="COAST 2" status="Normal"></Status>
        <Status name="DROGUE DEPLOYMENT" status="Waiting"></Status>
        <Status name="MAIN DEPLOYMENT" status="Waiting"></Status>
        <Status name="LANDED" status="Waiting"></Status>
      </div>
      <div className="second-column">
        <div className="header">
          <div id="title">Casper Vehicle Launch</div>
          <div id="timer-title">Mission Elapsed Timer</div>
          <Timer id="timer" hours="00" minute="00" seconds="00"></Timer>
        </div>
        <div className="body">Hey lol</div>
        <div className="foot">
          <div className='lines'>
            <BasicExample></BasicExample>
          </div>
          <div className ='connections'>Connections</div>
        </div>
      </div>
      <div className="third-column">
        <img id="casper-image" src= {require('./images/rocketBeta.png')} alt="Error: failed to load"/>
      </div>
    </div>
  );
}

export default App;

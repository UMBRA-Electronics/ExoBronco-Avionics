import './App.css';
import Timer from './components/Timer.jsx'
import Status from './components/Status.jsx'
import Dashboard from './components/Dashboard.jsx';
import PyroChannel from './components/PyroChannel.jsx';
import ProgressBar from './components/ProgressBar.jsx';

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
        <div className="body">
          <div className="body-first-row">
            <Dashboard value={2.69} max={20} color="green" type="VELOCITY" units="ft/s" width={150} class="dashboard"></Dashboard>
            <Dashboard value={30} max={40} color="orange" type="ACCELERATION" units="ft/s^2" width={150}></Dashboard>
            <Dashboard value={14.00} max={40} color="red" type="ALTITUDE" units="ft" width={150}></Dashboard>
            <Dashboard value={.07} max={.5} color="cyan" type="Pressure" units="psi" width={150}></Dashboard>
          </div>
          <div className="body-second-row">
            <Dashboard value={26.53} max={50} color="cyan" type="PITCH" units="Degrees" width={125}></Dashboard>
            <Dashboard value={20} max={50} color="cyan" type="YAW" units="Degrees" width={125}></Dashboard>
            <Dashboard value={0} max={40} color="cyan" type="PITCH GYRO" units="Degrees/s" width={125}></Dashboard>
            <Dashboard value={.07} max={.5} color="cyan" type="ALTITUDE" units="Degrees/s" width={125}></Dashboard>
          </div>
        </div>
        <div className="foot">
          <div className='lines-container'>
            <div id='other-info'>Other Info</div>
            <hr id="lineheader"></hr>
            <div className='progress-container'>
              <div className='line-title'>RSSI</div>
              <ProgressBar bgcolor="cyan" completed={-2} units="dbm" min={-5} max={0}></ProgressBar>
              <div className='line-title'>BMP390 Temperature</div>
              <ProgressBar bgcolor="cyan" completed={14.0} units="°F" min={0} max={100}></ProgressBar>
              <div className='line-title'>MS8607 Temperature</div>
              <ProgressBar bgcolor="cyan" completed={14.5} units="°F" min={0} max={100}></ProgressBar>
              <div className='line-title'>VBATT</div>
              <ProgressBar bgcolor="cyan" completed={14.7} units="V" min={0} max={30}></ProgressBar>
            </div>
          </div>
          <div className ='connections-container'>
            <div id="connections">Connections</div>
            <hr id="lineheader"></hr>
            <div className="pyro-container">
              <PyroChannel number='1' status="Connected"></PyroChannel>
              <PyroChannel number='2' status="Connected"></PyroChannel>
              <PyroChannel number='3' status="Connected"></PyroChannel>
              <PyroChannel number='4' status="Connected"></PyroChannel>
            </div>
          </div>
        </div>
      </div>
      <div className="third-column">
        <img id="casper-image" src= {require('./images/rocketBeta.png')} alt="Error: failed to load"/>
      </div>
    </div>
  );
}

export default App;

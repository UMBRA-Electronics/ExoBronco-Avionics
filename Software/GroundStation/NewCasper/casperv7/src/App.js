import './App.css';
import { useState, useEffect } from "react";
import Timer from './components/Timer.jsx'
import Status from './components/Status.jsx'
import Dashboard from './components/Dashboard.jsx';
import PyroChannel from './components/PyroChannel.jsx';
import ProgressBar from './components/ProgressBar.jsx';

function App() {

  const URL = 'https://www.randomnumberapi.com/api/v1.0/random?min=-32&max=32&count=1';
  const [results, setResults] = useState([]);
  
  useEffect(() => {
    async function getData() {
      const response = await fetch(URL);
      const data = await response.json();
      setResults(data);
    }

    getData();
  });

  return (
    <div className="App">
      <div id="packet-number">Packet Number: {69}</div>
      <div className="first-column">
        <Status name="COMMISIONING" status={1}></Status>
        <Status name="ON PAD" status={1}></Status>
        <Status name="MOTOR 1 BURN" status={1}></Status>
        <Status name="COAST 1" status={1}></Status>
        <Status name="MOTOR 2 IGNITION" status={2}></Status>
        <Status name="MOTOR 2 BURN" status={2}></Status>
        <Status name="COAST 2" status={1}></Status>
        <Status name="DROGUE DEPLOYMENT" status={0}></Status>
        <Status name="MAIN DEPLOYMENT" status={0}></Status>
        <Status name="LANDED" status={0}></Status>
      </div>
      <div className="second-column">
        <div className="header">
          <div id="title">Casper Vehicle Launch</div>
          <div id="timer-title">Mission Elapsed Timer</div>
          <Timer id="timer" hours="00" minute="00" seconds="00"></Timer>
        </div>
        <div className="body">
          <div className="body-first-row">
            <Dashboard value={results} min={-32} range={64} color="green" type="BNO ACCELERATION" units="ft/s" width={150} class="dashboard"></Dashboard>
            <Dashboard value={0} min={-100} range={200} color="orange" type="ADXL ACCELERATION" units="ft/s^2" width={150}></Dashboard>
            <Dashboard value={50000} min={0} range={100000} color="red" type="ALTITUDE" units="ft" width={150}></Dashboard>
            <Dashboard value={15} min={0} range={30} color="cyan" type="Pressure" units="psi" width={150}></Dashboard>
          </div>
          <div className="body-second-row">
            <Dashboard value={0} min={-180} range={360} color="cyan" type="PITCH" units="Degrees" width={125}></Dashboard>
            <Dashboard value={0} min={-180} range={360} color="cyan" type="YAW" units="Degrees" width={125}></Dashboard>
            <Dashboard value={0} min={-90} range={180} color="cyan" type="PITCH GYRO" units="Degrees/s" width={125}></Dashboard>
            <Dashboard value={0} min={-90} range={180} color="cyan" type="YAW GYRO" units="Degrees/s" width={125}></Dashboard>
          </div>
        </div>
        <div className="foot">
          <div className='lines-container'>
            <div id='other-info'>Other Info</div>
            <hr id="lineheader"></hr>
            <div className='progress-container'>
              <div className='line-title'>RSSI</div>
              <ProgressBar bgcolor="cyan" value={50} units="dbm" min={0} range={120}></ProgressBar>
              <div className='line-title'>Warning Flags</div>
              <ProgressBar bgcolor="cyan" value={50} units="°F" min={0} range={100}></ProgressBar>
              <div className='line-title'>Temperature</div>
              <ProgressBar bgcolor="cyan" value={50} units="°F" min={-40} range={165}></ProgressBar>
              <div className='line-title'>VBATT</div>
              <ProgressBar bgcolor="cyan" value={14} units="V" min={12} range={3}></ProgressBar>
            </div>
          </div>
          <div className ='connections-container'>
            <div id="connections">Connections</div>
            <hr id="lineheader"></hr>
            <div className="pyro-container">
              <PyroChannel number='1' status={0}></PyroChannel>
              <PyroChannel number='2' status={0}></PyroChannel>
              <PyroChannel number='3' status={1}></PyroChannel>
              <PyroChannel number='4' status={1}></PyroChannel>
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

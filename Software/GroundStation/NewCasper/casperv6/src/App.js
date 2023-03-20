import './App.css';

function App() {
  return (
    <div className="App">
      <div class="first-row">
        <div id="title">Casper V6</div>
          <div class="timer">
            <div id="timer-title">Mission Elapsed Timer</div>
            <div id="clock">00:00:00</div>
          </div>
      </div>
      <div className="second-row">
        <img src="https://www.freeiconspng.com/thumbs/rocket-ship-png/rocket-ship-png-7.png" alt="Rocket Ship" id = "rocketshipimage"></img>
        <div className="important-info-box">
          <div className="states-container">
              <div className ="circle active">1</div>
              <div className ="circle">2</div>
              <div className ="circle">3</div>
              <div className ="circle">4</div>
              <div className ="circle">5</div>
          </div>
          <div className = "pie-container">
            <div className="velocity-container">
              <div className="pie" id="velocity">42.0%</div>
              <div className="pie-title">Total Rocket Velocity</div>
            </div>
            <div className="acceleration-container">
              <div className="pie" id="acceleration">13%</div>
              <div className="pie-title">Acceleration</div>
            </div>
            <div className="pitch-container">
              <div className="pie" id="pitch">12%</div>
              <div className="pie-title">Pitch</div>
            </div>
            <div className="yaw-container">
              <div className="pie" id="yaw">99%</div>
              <div className="pie-title">Yaw</div>
            </div>
            <div className="gyro-container">
              <div className="pie" id="gyro">80%</div>
              <div className="pie-title">Gyro</div>
            </div>
            <div className="roll-container">
              <div className="pie" id="roll">10%</div>
              <div className="pie-title">Roll</div>
            </div>
          </div>
        </div>
        <div className="line-values">
          <div className="RSSI-container">
            <div id="RSSI">RSSI</div>
            <div className="line"></div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

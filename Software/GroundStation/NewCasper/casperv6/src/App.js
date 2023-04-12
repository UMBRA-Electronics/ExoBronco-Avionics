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
        <img src={require('./images/rocketBeta.png')} alt="Rocket Ship" id = "rocketshipimage"/>
          <div className="important-info-box">
            <div className = "container">
              <div className="progress-container">
                <div class="progress" id="progress"></div>
                <div className ="circle">1</div>
                <div className ="circle">2</div>
                <div className ="circle active">3</div>
                <div className ="circle">4</div>
                <div className ="circle">5</div>
              </div>
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
            <div className="bottom-half">
              <div className="pyro-channels">
                <div className="pyro-channel">
                  <div className="pyro-bubble">✔</div>
                  <div className="pyro-title">CH 1</div>
                </div>
                <div className="pyro-channel">
                  <div className="pyro-bubble">✔</div>
                  <div className="pyro-title">CH 2</div>
                </div>
                <div className="pyro-channel">
                  <div className="pyro-bubble">✔</div>
                  <div className="pyro-title">CH 3</div>
                </div>
                <div className="pyro-channel">
                  <div className="pyro-bubble">✔</div>
                  <div className="pyro-title">CH 4</div>
                </div>
                <div className="pyro-channel">
                  <div className="pyro-bubble">✔</div>
                  <div className="pyro-title">CH 5</div>
                </div>
              </div>
            </div>
          </div>
        <div className="line-values">
          <div className="line-container">
            <div class="line-title">RSSI</div>
            <div className="line"></div>
            <div className="point"></div>
            <div className="line-outline"></div>
            <div className="line-output">69Nice</div>
          </div>
          <div className="line-container">
            <div class="line-title">TEMP 1</div>
            <div className="line"></div>
            <div className="point"></div>
            <div className="line-outline"></div>
            <div className="line-output">420Nice</div>
          </div>
          <div className="line-container">
            <div class="line-title">TEMP 2</div>
            <div className="line"></div>
            <div className="point"></div>
            <div className="line-outline"></div>
            <div className="line-output">420Nice</div>
          </div>
          <div className="line-container">
            <div class="line-title">VBATT</div>
            <div className="line"></div>
            <div className="point"></div>
            <div className="line-outline"></div>
            <div className="line-output">420Nice</div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

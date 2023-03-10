import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Casper V6</h1>
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
          <div className = "kinematic-container">
            <div className="velocity-container">
              <div id="velocity">69.420m/s</div>
              <div id="velocity-title">Total Rocket Velocity</div>
            </div>
            <div className="acceleration-container">
              <div className="pie" id="acceleration">69%</div>
              <div id="acceleration-title">Acceleration</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

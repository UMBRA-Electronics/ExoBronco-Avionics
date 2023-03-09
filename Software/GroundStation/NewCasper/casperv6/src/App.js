import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Casper V6</h1>
      <div className="SecondRow">
        <img src="https://www.freeiconspng.com/thumbs/rocket-ship-png/rocket-ship-png-7.png" alt="Rocket Ship" id = "rocketshipimage"></img>
        <div className="ImportantInfoBox">
            <div className="States">
              <div id="State1"></div>
              <div id="State2"></div>
              <div id="State3"></div>
            </div>
            <div id="Velocity"></div>
            <div id="Acceleration"></div>
        </div>
      </div>
    </div>
  );
}

export default App;

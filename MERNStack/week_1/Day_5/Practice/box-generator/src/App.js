// import logo from './logo.svg';
import { useState } from 'react';
import './App.css';
import AddBox from './components/AddBox';
import Display from './components/Display';


function App() {
  const [boxes, setBoxes] = useState(["green", "blue", "purple"]);
  return (
    <div className="App">
      <AddBox boxes = {boxes}  setBoxes = {setBoxes} />
      <Display colors={(boxes)} />
    </div>
  );
}

export default App;

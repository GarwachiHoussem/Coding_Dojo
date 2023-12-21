import './App.css';
import PersonCard from './components/PersonCard';

function App() {
  const value1={
    firstName:"Houssem",
    lastName:"Garwachi",
    age: 28,
    hairColor:"black",
    birthday: "birthday"
  }
  const value2={
    firstName:"Houssem",
    lastName:"Garwachi",
    age: 28,
    hairColor:"black"
  }
  const value3={
    firstName:"Houssem",
    lastName:"Garwachi",
    age: 28,
    hairColor:"black"
  }
  return (
    <div className="App">
      <PersonCard props={value1}/>
      <PersonCard props={value2}/>
      <PersonCard props={value3}/>
    </div>
  );
}

export default App;
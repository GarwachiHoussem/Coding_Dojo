import "./App.css";
import PersonCard from "./components/PersonCard";

const peopleArr = [
  {
    firstName: "Houssem",
    lastName: "Gr",
    age: 45,
    hairColor: "Black",
  },
  {
    firstName: "aymen",
    lastName: "br",
    age: 88,
    hairColor: "Brown",
  },
  {
    firstName: "ahmed",
    lastName: "hz",
    age: 45,
    hairColor: "Black",
  },

];

function App() {
  return (
    <div className="App">
      {peopleArr.map((personObj, index) => (
        <PersonCard
          key={index}
          firstName={personObj.firstName}
          lastName={personObj.lastName}
          age={personObj.age}
          hairColor={personObj.hairColor}
        />
      ))}

    </div>
  );
}

export default App;

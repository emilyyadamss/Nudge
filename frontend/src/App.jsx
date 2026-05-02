import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [goals, setGoals] = useState([]) //runs once. 

  useEffect( () => {
    fetch( "http://localhost:8000/goals" )
      .then( response => response.json() ) // fetch makes a GET request to the backend. The response parses the JSON. 
      .then( data => setGoals(data) ) // stores the result in your goals state variable.
      .catch( error => console.error( 'Error fetching goals:', error ) ) // when the fetch request fails, it logs the error to the console.
  }, [] ) //empty dependency array means it runs once when the component mounts.

  return (
    <div> 
      <h1>Nudge</h1>
      { goals.map(goal => 
        <p key={goal.id}>{goal.name}</p>
      ) }
    </div>
  )
}

export default App

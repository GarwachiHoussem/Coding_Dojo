import React from 'react'

const PersonCard = ({props}) => {

    const value=props

  return (
    <div>
        {JSON.stringify(value)}
        <h1>{value.lastName},{value.firstName} </h1>
        <p>age :{value.age}</p>
        <p>hair color :{value.hairColor}</p>
        <button>birthday{value.birthday}</button>

    </div>
  )
}

export default PersonCard
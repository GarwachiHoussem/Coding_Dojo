import React from 'react'

const Display = (props) => {
  const couleurs = props.colors

  return (

    couleurs.map((el) =>{
      
      return ( < div style={{ width: "300px", height: "300px", background: el , display : "inline-block" , margin : "2px"}} > </div >)
    }
    )
    
    )
  

}

export default Display
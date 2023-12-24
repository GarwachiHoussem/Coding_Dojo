import React, { useState } from 'react'

const Form = () => {

    const [ firstname, setFirstname ] = useState('')
    const [ lastname, Setlastname ] = useState('')
    const [ email, Setemail ] = useState('')
    const [ password, Setpassword ] = useState('')
    const [ confirmpassword, Setconfirmpassword ] = useState('')

    const createUser = (e) => {
        // we must prevent the default refresh of the browser to keep our state from being reset
        e.preventDefault();
    };

    return (
        <fieldset>
        <form  onSubmit={ createUser }>
        <div>
                <label>firstname :</label> 
                <input type="text" onChange={ (e) => setFirstname(e.target.value) } />
            </div>
            <div>
                <label>lastname : </label> 
                <input type="text" value={lastname} onChange={ (e) => Setlastname(e.target.value) } />
            </div>
            <div>
                <label> email : </label> 
                <input type="email" value={email} onChange={ (e) => Setemail(e.target.value) } />
            </div>
            <div>
                <label> password :</label> 
                <input type="password" value={password} onChange={ (e) => Setpassword(e.target.value) } />
            </div>
            <div>
                <label> confirmpassword : </label> 
                <input type="confirmpassword" value={confirmpassword} onChange={ (e) => Setconfirmpassword(e.target.value) } />
            </div>
        </form>
        <div>
            <p>firstname:{firstname}</p>
            <p>lastname:{lastname}</p>
            <p>email:{email}</p>
            <p>password:{password}</p>
            <p>confirmpassword:{confirmpassword}</p>
        </div>
        </fieldset>
    )
}

export default Form
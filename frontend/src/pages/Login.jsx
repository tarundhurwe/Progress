import React from 'react'
import Form from '../components/Form'

const Login = () => {

    return (
        <>
            <Form route="/api/token/" method="Login" />
        </>
    )
}

export default Login
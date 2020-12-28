import React from 'react'
import { apiTweetCreate } from './lookup'

export function TweetCreate(props) {
    const textAreaRef = React.createRef()
    const { didTweet } = props

    // callback
    // change this to server side call
    const handleBackendUpdate = (response, status) => {
        // backend response api request handler
        if (status === 201) {
            // you can use pust but we get newest tweets on top so using unshift 
            didTweet(response)
        }
        else {
            alert("data not sended to backend something went wrong")
        }
    }
    const handleSubmit = (event) => {
        event.preventDefault()
        // this is will all tempnewTweet in newTweets which allready a var
        const newvalue = textAreaRef.current.value
        // backend response api request
        apiTweetCreate(newvalue, handleBackendUpdate)
        textAreaRef.current.value = ''
    }
    return <div className='container'>
        <div className="container mt-5 p-2">
            <h1 className='offset-1' > Welcome on react tweets </h1>
        </div>

        {/* this is the main concept */}
        <div className={props.className}>
            <form onSubmit={handleSubmit} >
                <textarea ref={textAreaRef} required={true} className='form-control' placeholder=' tweet here....' ></textarea>
                <button type='submit' className='btn btn-primary my-3'> tweet </button>
            </form>
        </div>
        {/* {...props } is pass self props */}
    </div>

}

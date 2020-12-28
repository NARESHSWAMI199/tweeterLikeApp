
import {apiTweetAction } from './lookup'

export function ActionButton(props) {
    const { tweet, action, didPerformAction } = props
    const likes = tweet.likes ? tweet.likes : 0
    const actionDisplay = action.display ? action.display : "Action"
    const display = action.display === 'likes' ? `${likes} ${action.display}` : actionDisplay
    const className = props.className ? props.className : 'btn shadow-sm btn-primary'


    const handleActionBackendEvent = (response, status) => {
        console.log("response ", response, "status ", status)
        if ((status === 200 || status === 201) && didPerformAction) {
            didPerformAction(response, status)
        }
    }


    // this is function like lamda in python
    const handleClick = (event) => {
        event.preventDefault()
        apiTweetAction(tweet.id, action.type, handleActionBackendEvent)
    }

    return <button className={className} onClick={handleClick} >   {display}   </button>
}
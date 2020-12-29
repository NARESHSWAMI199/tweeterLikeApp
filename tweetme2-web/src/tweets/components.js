import React, { useEffect,useState } from 'react'
import { TweetList } from './list'
import {TweetCreate} from './create'
import {apiTweetDetail} from './lookup'
import { Tweet } from './detail'
import {TweetFeedList} from './feed'
import {} from '..'





export function TweetFeedConponents(props) {
    const [newTweets, setnewTweets] = useState([])
    // change this to server side call
    const canTweet = props.canTweet === "false" ? false : true

    const handleNewTweet = (newTweet) => {
        let tempNewTweet = [...newTweets]
        // backend response api request handler
        // you can use pust but we get newest tweets on top so using unshift 
        tempNewTweet.unshift(newTweet)
        setnewTweets(tempNewTweet)
    }
    return <div className='container'>
        {canTweet === true && <TweetCreate didTweet={handleNewTweet} className='col-10 offset-1' ></TweetCreate>}
        {/*  {...props } is pass self props  */}
        <TweetFeedList newTweets={newTweets} {...props} />
    </div>
}







// this function have username and can tweet beacuse we have mantion in api class
// this function showing our data on react page 
export function TweetConponents(props) {
    const [newTweets, setnewTweets] = useState([])
    // change this to server side call
    const canTweet = props.canTweet === "false" ? false : true

    const handleNewTweet = (newTweet) => {
        let tempNewTweet = [...newTweets]
        // backend response api request handler
        // you can use pust but we get newest tweets on top so using unshift 
        tempNewTweet.unshift(newTweet)
        setnewTweets(tempNewTweet)
    }
    return <div className='container'>
        {canTweet === true && <TweetCreate didTweet={handleNewTweet} className='col-10 offset-1' ></TweetCreate>}
        {/*  {...props } is pass self props  */}
        <TweetList newTweets={newTweets} {...props} />
    </div>
}


export function TweetDetailComponent(props){
    const {tweetId} = props
    const [didLookup,setDidLookup] = useState(false)
    const [tweet,setTweet] = useState(null)

    const handleBackendLookup = (response,status)=>{
        console.log("the status : ",response,status)
        if (status === 200){
            setTweet(response)
        }else{
            alert("there is a error to finding your tweet")
        }
    }

    useEffect(()=>{
        if (didLookup === false){
            apiTweetDetail(tweetId,handleBackendLookup)
            setDidLookup(true)
        }
    },[didLookup,setDidLookup,tweetId])

    return tweet === null ? null : <Tweet tweet = {tweet} className={props.className}></Tweet>
}
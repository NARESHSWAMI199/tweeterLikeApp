import React, { useEffect, useState } from 'react'
import { apiTweetList } from './lookup'
import { Tweet } from './detail'



export function TweetList(props) {
    // use effect take a function as a argument
    const [tweetsInit, setTweetInit] = useState([])
    const [tweets, setTweets] = useState([])
    // this is important when you use respone pagination  beacuse pagination provide we 
    //  a next page url
    const [nextUrl, setNextUrl] = useState(null)
    const [tweetDidSet, setTweetDidsSet] = useState(false)
    // we going another useEffect for newTweet
    useEffect(() => {
        const final = [...props.newTweets].concat(tweetsInit)
        if (final.length !== tweets.length) {
            setTweets(final)
        }
    }, [props.newTweets, tweets, tweetsInit])

    useEffect(() => {
        if (tweetDidSet === false) {
            const handleTweetListLookup = (response, status) => {
                if (status === 200) {
                    // i added here results after pagination
                    setNextUrl(response.next)
                    setTweetInit(response.results)
                    setTweetDidsSet(true)
                }
                else {
                    alert('an error accur')
                }
            }

            apiTweetList(props.username, handleTweetListLookup)
        }

    }, [tweetsInit, tweetDidSet, setTweetDidsSet, props.username])
    // setTweetInit([...newTweets].concat(tweetInit))

    const handleDidRetweet = (newTweet) => {
        const updateTweetsInit = [...tweetsInit]
        updateTweetsInit.unshift(newTweet)
        setTweetInit(updateTweetsInit)

        const updateFinalTweets = [...tweets]
        updateFinalTweets.unshift(tweets)
        setTweets(updateFinalTweets)
    }

    const handleLoadNext = (event) => {
        event.preventDefault()
        if (nextUrl !== null) {
            const handleLoadNextResponse = (response, status) => {
                if (status === 200) {
                    // i added here results after pagination
                    setNextUrl(response.next)
                    // this step will load our all tweets on same page
                    const newTweets = [...tweets].concat(response.results)
                    setTweetInit(newTweets)
                    setTweets(newTweets)
                }
                else {
                    alert('an error accur')
                }
            }
            // here first argument is username a secound is the user 
            apiTweetList(props.username, handleLoadNextResponse, nextUrl)
        }

    }

    // we show all tweets's in a fregment beacuse we going create a load button
    return <React.Fragment>
        {tweets.map((items, index) => {
            return <Tweet tweet={items}
                didRetweet={handleDidRetweet}
                className='py-5 px-5 mt-1 border-radius shadow-sm  bg-white text-dark'
                key={`${index}-{item.id}`} />
        })}
        {nextUrl !== null && <button onClick={handleLoadNext} className="btn mt-5 mb-5 btn-outline-primary">Load More ...</button>}
    </React.Fragment>
}

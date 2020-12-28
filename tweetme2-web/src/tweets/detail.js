import React, { useState } from 'react'
import { ActionButton } from './buttons'
import { UserDisplay,UserLink,UserPicture } from "../profiles/"


export function ParentTweet(props) {
    const { tweet } = props
    return tweet.parent ? <Tweet retweeter={props.retweeter} isRetweet hideActions className={' '} tweet={tweet.parent} /> : null
}


// this fuction we calling where we rendering or where we calling map function AS A Tweet tag
// THIS FUNCTION SHOWING OUR DATA IN PROPER WAY
// and here if you call a function as like a tag you must need use props






export function Tweet(props) {
    const { tweet, didRetweet, hideActions, isRetweet, retweeter } = props
    const [actionTweet, setActionTweet] = useState(props.tweet ? props.tweet : null)


    const path = window.location.pathname
    const idRegex = /(?<tweetid>\d+)/
    const match = path.match(idRegex)
    const urlTweetId = match ? match.groups.tweetid : -1

    const isDetail = `${tweet.id}` === `${urlTweetId}`

    const handleLink = (event) => {
        event.preventDefault()
        window.location.href = `/${tweet.id}`
    }

    const handlePerformAction = (newActionTweet, status) => {
        console.log('newAction tweet ', newActionTweet, status)
        if (status === 200) {
            setActionTweet(newActionTweet)
        } else if (status === 201) {
            if (didRetweet) {
                didRetweet(newActionTweet)
            }
        }
    }
    // this is check if class exists then return same else we given
    // this is a ternary opreator or you can say  ? same like java
    const className = props.className ? props.className : 'col-10 mx-auto p-3 col-md-6'
    return <div className={className}>
        {isRetweet === true && <div className='col-12 mb-3'> <span className='small text-muted' > Retweet Via  @ <UserDisplay user={retweeter} /> </span>  </div>}
        <div className='d-flex' >
            <UserPicture user={tweet.user} ></UserPicture>
            <div className="col-11">
                {/* <p> {tweet.user.first_name}{' '}
                    {tweet.user.last_name}{' '}
                    @{tweet.user.username} </p> */}
             <UserLink username={tweet.user.username}><UserDisplay includeFullName user={tweet.user} /></UserLink>   
                <p>{tweet.content} </p>
                <ParentTweet tweet={tweet} retweeter={tweet.user} />
            </div>
        </div>

        <div className="btn btn-group" >
            {/* we create a fregment for only action buttoons */}
            {(actionTweet && hideActions !== true) && <React.Fragment>
                <ActionButton tweet={actionTweet} didPerformAction={handlePerformAction} action={{ type: "like", display: 'likes' }} />
                <ActionButton tweet={actionTweet} didPerformAction={handlePerformAction} action={{ type: "unlike", display: 'unlike' }} />
                <ActionButton tweet={actionTweet} didPerformAction={handlePerformAction} action={{ type: "retweet", display: 'retweet' }} />
            </React.Fragment>}

            {isDetail === true ? null : < button className=' btn btn-sm btn-outline-primary' onClick={handleLink}> view </button>}
        </div>
    </div>
}

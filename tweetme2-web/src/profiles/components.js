import React from 'react'

export function UserDisplay(props) {
    const { user, includeFullName, hidelink } = props
    const fullname = includeFullName === true ? `${user.first_name} ${user.last_name}` : null
    return <React.Fragment>
        {fullname}
        {hidelink === true ? `@${user.username}` : <UserLink username={user.username}> @{user.username} </UserLink>}
    </React.Fragment>
}


export function UserLink(props) {
    const { username } = props
    // event is a defalut arg when you click a button or perfom and event
    const handleUserLink = (event) => {
        window.location.href = `profiles/${username}/`
    }
    return <span className="pointer" onClick={handleUserLink}>
        {props.children}
    </span>
}


// user pictrue calling in Tweet
export function UserPicture(props) {
    const { user, hidelink } = props
    const profileSpan = <span className='px-3 py-2 rounded-circle text-white bg-dark' >{user.username[0]}</span>
    return hidelink === true ? profileSpan : <UserLink username={user.username} >{profileSpan}</UserLink>

}
// Numeral is react or npm package which allow you a large number like 20573894-67957 convert into  2m or 2cr 
import numeral from 'numeral'
// this function make for only show my data in a valid or nice format
export    function DisplayCount(props){
     return  <span className={props.className}> {numeral(props.children).format("0a")} </span>
 }
   
 
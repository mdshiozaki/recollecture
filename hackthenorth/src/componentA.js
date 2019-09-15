import React from 'react'

class ComponentA extends React.Component {
    
    constructor(props) {
        super(props);
        this.state = {
            display: 'Hello Friendo!',
            toggle: true

        }

        this.clickHandler = this.clickHandler.bind(this)
        
    }

    clickHandler(){
        let newState=Object.assign({}, this.state) //making copy of code
        newState.toggle = !newState.toggle
        newState.display = newState.toggle ? 'Hello Friendo' : 'Goodbye Friendo'
        this.setState(newState)
    }

    render (){
        return(
            <div className='componentA'>

                {this.state.display}

                <button onClick={this.clickHandler}>

                 {this.state.toggle ? 'ON' : 'OFF'}


                 </button>
              
            </div>

            
        )
    
    }
}

export default ComponentA
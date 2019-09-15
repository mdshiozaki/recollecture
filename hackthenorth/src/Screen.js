import SideNav, { Toggle, Nav, NavItem, NavIcon, NavText } from '@trendmicro/react-sidenav';
import React from 'react';
import './Screen.css';
// Be sure to include styles at some point, probably during your bootstraping
import '@trendmicro/react-sidenav/dist/react-sidenav.css';
import clipboard1 from './assets/clipboard1.png';
import clipboard2 from './assets/clipboard2.png';
import clipboard3 from './assets/clipboard3.png';
import clipboard4 from './assets/clipboard4.png';

class Screen extends React.Component {
    
    //parenthesis - means it is a function
    // if not then it is a field

    render() {
        return (

            <SideNav>
                <SideNav.Toggle />
                    < SideNav.Nav>
                    <NavItem eventKey="home" className="individual-icon" >
                        <NavIcon >
                            <img src={clipboard1} className="icon-sidebar"/>
                        </NavIcon>
                        <NavText>
                            SYDE 101
                        </NavText>
                    </NavItem>
                    
                    <NavItem eventKey="charts" className="individual-icon" >
                        <NavIcon>
                        <img src={clipboard2} class="icon-sidebar"/>
                        </NavIcon>
                        <NavText>
                            SYDE 161
                        </NavText>
                    </NavItem>
                        
                    <NavItem eventKey="charts" className="individual-icon" >
                        <NavIcon>
                        <img src={clipboard3} class="icon-sidebar"/>
                        </NavIcon>
                        <NavText>
                        PSYCH 101
                        </NavText>
                    </NavItem>
                        

                    <NavItem eventKey="charts" className="individual-icon" >
                        <NavIcon>
                        <img src={clipboard4} class="icon-sidebar"/>
                        </NavIcon>
                        <NavText>
                        HTN 19 
                        </NavText>
                    </NavItem>
         
                </SideNav.Nav>
            </SideNav>
            
           
        );
    }
}



export default Screen;
import KvmDeviceList from "./KvmDeviceList";
import KvmGuestList from './KvmGuestList';
import DCFooter from './DCFooter';

import '../css/MainBody.css';
function MainBody() {
    return (
        <div className="MainBody">
            <div className="DisplayArea">
                <div className="LeftSide">
                    <KvmDeviceList />
                    <KvmGuestList />
                </div>
                <div className="RightSide">
                    <h3>right display</h3>
                    {/* <div className="MainDisplay"><h1>main display</h1></div> */}
                </div>
            </div>
            <DCFooter />
        </div>
    )
}
export default MainBody;
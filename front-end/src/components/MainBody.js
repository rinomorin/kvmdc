import KVMNodes from './KVMNodes';
import KVMVms from './KVMVms';
import DCFooter from './DCFooter';

import '../css/MainBody.css';
function MainBody() {
    return (
        <div className="MainBody">
            <div className="DisplayArea">
                <div className="LeftSide">
                    <KVMNodes />
                    <h1><test  </h1>
                    // <KVMVms />
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
import DCHeader from './DCHeader';
import DCMenu from './DCMenu';
import MainBody from './MainBody';

import '../css/DCBody.css';

function DCBody() {
    return (
    <div className="DCBody">
        <DCHeader />
        <DCMenu />
        <MainBody />
    </div>
    )
}
export default DCBody;
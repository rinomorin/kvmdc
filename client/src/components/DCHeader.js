import DropdownMenu from './DropdownMenu';

import '../css/DCHeader.css';
function DCHeader() {
    return (
        <div className="DCHeader">
            <DropdownMenu />
            <h3 className="DCHeaderTitle">KVM Datacenter Console</h3>
            <div className="DCAuth"><h3><span>login</span></h3></div>
        </div>
    )
}

export default DCHeader;
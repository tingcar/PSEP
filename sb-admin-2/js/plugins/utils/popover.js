$(function(){
	$(".h5a-sidebar").affix({offset:{top:-10,bottom:function(){return this.bottom=$(".bs-footer").outerHeight(!0)}}}),$(".popover-test").popover({trigger:"hover",html:!0}),$(".tooltip-test").tooltip({html:!0})});
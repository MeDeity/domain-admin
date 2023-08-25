import{C as w}from"./ConnectStatus.422775f5.js";import{_ as m}from"./index.02f2bb40.js";import{ah as l,o as _,c as f,V as a,P as n,a as c,U as p,ar as z,Q as y,T as k}from"./vendor-vue.0022cd7b.js";import"./element-icon.5bad8d92.js";import"./vendor-lib.acf3059b.js";import"./element-plus.b25ca83b.js";const $={name:"",components:{ConnectStatus:w},props:{list:{type:Array}},computed:{},data(){return{currentRow:null,dialogVisible:!1}},methods:{handleEditRow(t){this.currentRow=t,this.dialogVisible=!0},async handleDeleteClick(t){let e={id:t.id};const i=await this.$http.function(e);i.code==0?(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.$emit("on-success")):this.$msg.error(i.msg)},async handleStatusChange(t){let e={id:t.id};const i=await this.$http.function(e);i.code==0?(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.$emit("on-success")):this.$msg.error(i.msg)},handleUpdateSuccess(){this.$emit("on-success")}},created(){}};function v(t,e,i,S,o,d){const r=l("el-table-column"),h=l("ConnectStatus"),u=l("el-table");return _(),f("div",null,[a(u,{data:i.list,stripe:"",border:""},{default:n(()=>[a(r,{label:"\u5E8F\u53F7",align:"center",prop:"id",width:"60"},{default:n(s=>[c("span",null,p(s.$index+1),1)]),_:1}),a(r,{label:"\u5F00\u59CB\u65F6\u95F4","header-align":"center",align:"center",prop:"create_time"},{default:n(s=>[c("span",null,p(s.row.create_time||"-"),1)]),_:1}),a(r,{label:"\u7ED3\u675F\u65F6\u95F4","header-align":"center",align:"center",prop:"update_time"},{default:n(s=>[c("span",null,p(s.row.update_time||"-"),1)]),_:1}),a(r,{label:"\u6301\u7EED\u65F6\u95F4","header-align":"center",align:"center",prop:"total_time_label"},{default:n(s=>[c("span",null,p(s.row.total_time_label||"-"),1)]),_:1}),a(r,{label:"\u72B6\u6001","header-align":"center",align:"center",prop:"status",width:"60"},{default:n(s=>[a(h,{value:s.row.status},null,8,["value"])]),_:1}),a(r,{label:"\u9519\u8BEF\u4FE1\u606F","header-align":"center",align:"center",prop:"status"},{default:n(s=>[c("span",null,p(s.row.error_message||"-"),1)]),_:1})]),_:1},8,["data"])])}const x=m($,[["render",v]]),V={name:"log-scheduler-list",props:{},components:{DataTable:x},data(){return{list:[],total:0,page:1,size:20,keywords:"",loading:!0,dialogVisible:!1,pageSizeCachekey:"pageSize"}},computed:{},methods:{resetData(){this.page=1,this.getData()},refreshData(){this.getData()},async getData(){this.loading=!0;let t={ticket:this.ticket,page:this.page,size:this.size,keywords:this.keywords};const e=await this.$http.getLogSchedulerList(t);e.code==0&&(this.list=e.data.list,this.total=e.data.total),this.loading=!1},handleAddRow(){this.dialogVisible=!0},handleAddSuccess(){this.resetData()},handleSizeChange(t){localStorage.setItem(this.pageSizeCachekey,t),this.resetData()},loadPageSize(){let t=localStorage.getItem(this.pageSizeCachekey);t&&(this.size=parseInt(t))},async handleBatchDeleteConfirm(){let t=this.$loading({fullscreen:!0});try{const e=await this.$http.clearLogSchedulerList();e.code==0?(this.$msg.success("\u64CD\u4F5C\u6210\u529F"),this.resetData()):this.$msg.error(e.msg)}catch(e){console.log(e)}finally{this.$nextTick(()=>{t.close()})}}},created(){this.loadPageSize(),this.getData()}},T={class:"app-container"},B={class:"flex justify-between mb-sm"},L=c("div",null,null,-1);function P(t,e,i,S,o,d){const r=l("Delete"),h=l("el-icon"),u=l("el-link"),s=l("el-popconfirm"),b=l("DataTable"),C=l("el-pagination"),D=z("loading");return _(),f("div",T,[c("div",B,[L,a(s,{title:"\u786E\u5B9A\u6E05\u7A7A\u65E5\u5FD7\uFF1F",onConfirm:d.handleBatchDeleteConfirm},{reference:n(()=>[a(u,{underline:!1,type:"danger",class:"mr-sm"},{default:n(()=>[a(h,null,{default:n(()=>[a(r)]),_:1}),k("\u6E05\u7A7A\u65E5\u5FD7")]),_:1})]),_:1},8,["onConfirm"])]),y(a(b,{list:o.list,onOnSuccess:d.resetData},null,8,["list","onOnSuccess"]),[[D,o.loading]]),a(C,{class:"mt-md justify-center",background:"",layout:"total, sizes, prev, pager, next",total:o.total,"page-size":o.size,"onUpdate:pageSize":e[0]||(e[0]=g=>o.size=g),"current-page":o.page,"onUpdate:currentPage":e[1]||(e[1]=g=>o.page=g),onCurrentChange:d.getData,onSizeChange:d.handleSizeChange},null,8,["total","page-size","current-page","onCurrentChange","onSizeChange"])])}const E=m(V,[["render",P]]);export{E as default};

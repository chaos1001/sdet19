<template>
  <v-data-table
    v-model="selected"
    :single-select="singleSelect"
    item-key="id"
    show-select
    :headers="headers"
    :items="desserts"
    sort-by="calories"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>测试用例</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-btn
              color="green"
              dark
              class="mb-2"
              @click="executeTestcase"
            >
              执行用例
            </v-btn>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              新增用例
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.id"
                      label="用例ID"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.node_id"
                      label="nodeid"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.remark"
                      label="备注"
                    ></v-text-field>
                  </v-col>

                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="save"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5">确定删除用例？</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
    <template v-slot:no-data>
      <v-btn
        color="primary"
        @click="initialize"
      >
        Reset
      </v-btn>
    </template>
  </v-data-table>
</template>

<script>
  export default {
    data: () => ({
      singleSelect: false,
      selected: [],
      dialog: false,
      dialogDelete: false,
      headers: [
        {
          text: '用例ID',
          align: 'start',
          sortable: false,
          value: 'id',
        },
        { text: 'nodeid', value: 'node_id' },
        { text: '备注', value: 'remark' },
        { text: 'Actions', value: 'actions', sortable: false },
      ],
      desserts: [],
      editedIndex: -1,
      editedItem: {
        id: '',
        node_id: 0,
        remark: 0,
      },
      defaultItem: {
        id: '',
        node_id: 0,
        remark: 0,
      },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? '新建用例' : '编辑用例'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    created () {
      this.initialize()
    },

    methods: {

      initialize () {
        // then方法 可以直接获取接口的响应值信息
        // result 代表接口的返回信息
        this.$api.testcase.getTestcase().then((result) => {
          this.desserts = result.data.msg.data
          console.log("获取用例列表接口", result.data.msg.data)
        }).catch((err) => {
          console.log("获取测试用例接口异常", err)
        });
        // this.desserts 决定了测试列表渲染的数据信息
      },

      editItem (item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },
      // 删除用例方法
      deleteItemConfirm () {
        console.log(this.editedItem)
        // 获取删除的id
        let delId = this.editedItem.id
        console.log("delId", delId)
        this.$api.testcase.deleteTestcase({"id": delId}).then((result) => {
            // 获取到响应信息，确定响应信息正确后，刷新页面
            if (result.data.code === 0){
              //刷新页面
              this.initialize()
            }
        }).catch((err) => {
          console.log(err)
        });
        this.closeDelete()
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
        if (this.editedIndex > -1) {
          //编辑用例的操作
          console.log("this.editedIndex > -1")
          console.log(this.editedItem)
          this.$api.testcase.updateTestcase(this.editedItem).then((result) => {
            // 判断是否有响应信息，且响应信息正确
            if (result.data.code === 0){
              //刷新页面
              this.initialize()
            }
          }).catch((err) => {
            console.log("调用修改用例接口异常, 异常信息为：", err)
            
          });

        } else {
          //新增用例
          console.log("else")
          console.log(this.editedItem)
          // 给用例列表添加了数据信息
          this.$api.testcase.addTestcase(this.editedItem).then((result) => {
            console.log(result)
            //当用例数据添加成功之后，还需要手动刷新
            // 判断是否有响应信息，且响应信息正确
            if (result.data.code === 0){
              //刷新页面
              this.initialize()
            }
          }).catch((err) => {
            console.log("添加用例接口异常，异常信息为：", err)
            
          });

        }
        this.close()
      },
      //执行用例
      executeTestcase(){
        //调用执行用例接口, 
        // axios.get("qtestcase")
        console.log("执行用例操作")
        console.log(this.selected)
      }
    },
  }
</script>
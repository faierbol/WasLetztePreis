<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>
        Adverts
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-text-field v-model="search" label="Search" class="mx-4"></v-text-field>
    <v-data-table :headers="headers" :items="adverts" :search="search">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.title }}</td>
        <td>{{ props.item.description }}</td>
        <td>{{ props.item.price }}</td>
        <td>{{ props.item.category }}</td>
        <td>{{ props.item.location }}</td>
        <td>{{ props.item.rating }}</td>
        <td class="justify-center layout px-0">
          <v-tooltip top>
            <span>Info</span>
            <v-btn slot="activator" flat :to="{name: 'main-adverts-detail', params: {id: props.item.id}}">
              <v-icon>info</v-icon>
            </v-btn>
          </v-tooltip>
        </td>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { readAdminAdverts } from '@/store/admin/getters';
import { dispatchGetAdverts } from '@/store/admin/actions';

@Component
export default class Adverts extends Vue {
  public search = '';
  public headers = [
    {
      text: 'Title',
      sortable: true,
      value: 'title',
      align: 'left',
    },
    {
      text: 'Description',
      sortable: true,
      value: 'description',
      align: 'left',
    },
    {
      text: 'Price',
      sortable: true,
      value: 'price',
      align: 'left',
    },
    {
      text: 'Category',
      sortable: true,
      value: 'category',
      align: 'left',
    },
    {
      text: 'Location',
      sortable: true,
      value: 'location',
      align: 'left',
    },
    {
      text: 'Rating',
      sortable: true,
      value: 'rating',
      align: 'left',
    },
    {
      text: 'Actions',
      value: 'id',
    },
  ];
  get adverts() {
    return readAdminAdverts(this.$store);
  }

  public redirectToDetail() {
    this.$router.push('main/dashboard');

  }

  public async mounted() {
    await dispatchGetAdverts(this.$store);
  }
}
</script>

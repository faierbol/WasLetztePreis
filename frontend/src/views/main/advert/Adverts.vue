<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>
        Adverts
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/adverts/create">Create Advert</v-btn>
    </v-toolbar>
    <v-text-field v-model="search" label="Search" class="mx-4"></v-text-field>
    <v-data-table :headers="headers" :items="adverts" :search="search">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.title }}</td>
        <td>{{ props.item.description }}</td>
        <td>{{ props.item.price }}</td>
        <td>{{ props.item.category }}</td>
        <td>{{ props.item.location }}</td>
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
import { readAdverts } from '@/store/main/getters';
import { dispatchGetAdverts } from '@/store/main/actions';
import { FB_ANALYTICS, FB_PERFORMANCE } from '@/firebase';

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
      text: 'Actions',
      value: 'id',
    },
  ];
  get adverts() {
    return readAdverts(this.$store);
  }

  public redirectToDetail() {
    this.$router.push('main/dashboard');

  }

  public async mounted() {
    FB_ANALYTICS.logEvent('Adverts called');
    const trace = FB_PERFORMANCE.trace('AdvertsTraced');
    trace.start();
    await dispatchGetAdverts(this.$store);
    trace.stop();
  }
}
</script>

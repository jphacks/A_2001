<template>
  <b-container>
    <b-card>
      <b-row>
        <b-col>
          <h3>guild title</h3>
          <p>descriotion</p>
          <div>
            <b-form-rating
              id="rating-readonly"
              class="p-0"
              value="3.6536"
              readonly
              no-border
              inline
              size="sm"
            ></b-form-rating>
            <p class="d-inline mb-1 text-muted">100 downloads</p>
          </div>
          <b-button type="button" variant="primary" size="sm"
            >download</b-button
          >
        </b-col>
      </b-row>
      <hr />
      <b-row>
        <b-col>
          <b-list-group>
            <b-list-group-item>task1</b-list-group-item>
            <b-list-group-item>task2</b-list-group-item>
            <b-list-group-item>task3</b-list-group-item>
            <b-list-group-item>task4</b-list-group-item>
          </b-list-group>
        </b-col>
      </b-row>
    </b-card>
  </b-container>
</template>

<script>
export default {};
</script>

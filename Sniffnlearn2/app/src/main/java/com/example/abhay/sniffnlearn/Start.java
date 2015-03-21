package com.example.abhay.sniffnlearn;

import android.app.SearchManager;
import android.content.Context;
import android.content.Intent;
import android.graphics.drawable.Drawable;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ListView;
import android.widget.SearchView;
import android.widget.Toast;


public class Start extends ActionBarActivity implements  SearchView.OnQueryTextListener {
    SearchView search;
    ListView recent, top;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_start);
        Drawable bg = findViewById(R.id.scroller).getBackground();
        bg.setAlpha(80);
        initialize();
    }

    public void initialize() {
        search = (SearchView) findViewById(R.id.search);
        // Assumes current activity is the searchable activity
        search.setIconifiedByDefault(false);
        recent = (ListView) findViewById(R.id.lvRecent);
        top = (ListView) findViewById(R.id.lvTop);
        search.setOnQueryTextListener(this);
    }

    @Override
    public boolean onQueryTextSubmit(String query) {
        Toast.makeText(getBaseContext(), query, Toast.LENGTH_SHORT).show();
        Intent myIntent = new Intent(Start.this, Results.class);
        myIntent.putExtra("query", query); //Optional parameters
        Start.this.startActivity(myIntent);
        return false;
    }

    @Override
    public boolean onQueryTextChange(String newText) {
        return false;
    }
}



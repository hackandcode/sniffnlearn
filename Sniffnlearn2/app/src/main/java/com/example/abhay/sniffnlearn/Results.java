package com.example.abhay.sniffnlearn;

import android.content.Intent;
import android.graphics.drawable.Drawable;
import android.net.Uri;
import android.os.Bundle;
import android.support.v7.app.ActionBarActivity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.List;


public class Results extends ActionBarActivity implements AdapterView.OnItemClickListener {
    ListView coursera,udacity,amazon,paper;
    List<String> animals;
    String query,responseText;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_results);
        Drawable bg=findViewById(R.id.scroller).getBackground();
        bg.setAlpha(80);
        intialize();
    }

    private void intialize() {
        Intent i= getIntent();
        query=i.getStringExtra("query");
        coursera=(ListView)findViewById(R.id.lvCoursera);
        udacity=(ListView)findViewById(R.id.lvUdacity);
        amazon=(ListView)findViewById(R.id.lvAmazon);
        paper=(ListView)findViewById(R.id.lvPaper);
        animals=new ArrayList<String>();
        getAnimalNames();
        ArrayAdapter<String> arrayAdapter =new ArrayAdapter<String>(this,R.layout.mylistheight, animals);
        coursera.setAdapter(arrayAdapter);
        coursera.setOnItemClickListener(this);
    }

    private void getreply() {
        HttpResponse response = null;
        try {
            HttpClient client = new DefaultHttpClient();
            HttpGet request = new HttpGet();
            request.setURI(new URI("http://192.168.14.247?"+query.replace(' ','+')));
            response = client.execute(request);
        } catch (URISyntaxException e) {
            e.printStackTrace();
        } catch (ClientProtocolException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

    }

    void getAnimalNames()
    {
        animals.add("DOG");
        animals.add("CAT");
        animals.add("HORSE");
        animals.add("ELEPHANT");
        animals.add("LION");
    }

    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("http://www.google.com"));
        startActivity(browserIntent);
    }
}

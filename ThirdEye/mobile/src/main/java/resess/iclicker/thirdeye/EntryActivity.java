package resess.iclicker.thirdeye;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import java.net.URI;
import java.net.URISyntaxException;

public class EntryActivity extends AppCompatActivity {

    private Button btnNextAct;
    public static final String TAG = "EntryActivity";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_entry);

        btnNextAct = findViewById(R.id.btn_next_act);
        btnNextAct.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(EntryActivity.this, SnapLoginAct.class);
                startActivity(i);
            }
        });

        try {
//            URI uri = new URI("myapp://snap-kit/oauth2");
            URI uri = new URI("https://www.google.com/");

            String temp = uri.getHost();
            Log.d(TAG,"host:  "+temp+" path: "+uri.getPath()+" scheme: "+uri.getScheme());
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }
    }
}
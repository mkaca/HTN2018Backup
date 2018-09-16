package resess.iclicker.thirdeye;

import android.content.Intent;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

public class SplashScreen extends AppCompatActivity {

    public ViewPager viewPager;

    public static final String TAG = "SplashScreen";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash_screen);

        viewPager = findViewById(R.id.pager);
        Button btn = findViewById(R.id.btn_main_activity);
        final PageAdapter pageAdapter = new PageAdapter(getSupportFragmentManager());
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Log.d(TAG,"Inside SplashScreen");

                viewPager.setAdapter(pageAdapter);
//                Intent intent = new Intent(SplashScreen.this, MainActivity.class);
//                startActivity(intent);
            }
        });
    }


    @Override
    protected void onResume() {
        super.onResume();
    }
}

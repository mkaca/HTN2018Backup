package resess.iclicker.thirdeye;

import android.content.Intent;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import com.bumptech.glide.Glide;
import com.snapchat.kit.sdk.SnapLogin;
import com.snapchat.kit.sdk.login.models.MeData;
import com.snapchat.kit.sdk.login.models.UserDataResponse;
import com.snapchat.kit.sdk.login.networking.FetchUserDataCallback;

import java.util.Map;

public class SnapLoginAct extends AppCompatActivity {

    public static final String TAG = "SnapLoginAct";
    private Button btnConnectSnap;
    private ImageView imgView;
    private View view;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_snap_login);
        getSupportActionBar().hide(); //<< this

        view = findViewById(R.id.view_act);
        imgView = findViewById(R.id.img_bitmoji_image);
        btnConnectSnap = findViewById(R.id.btn_add_snapchat);
        btnConnectSnap.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                SnapLogin.getAuthTokenManager(SnapLoginAct.this).startTokenGrant();
            }
        });

        view.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(SnapLoginAct.this, MapandTrack.class);
                startActivity(i);
            }
        });

        retrieveNameAndBitmoji();
    }

    public void retrieveNameAndBitmoji()
    {
        Log.d(TAG,"reaching here");

        String query = "{me{bitmoji{avtar},displayName}}";
        String var = null;  // check the next line null if val is to be replaced somehow
        SnapLogin.fetchUserData(this, query, null, new FetchUserDataCallback() {
            @Override
            public void onSuccess(@Nullable UserDataResponse userDataResponse) {
                if(userDataResponse==null || userDataResponse.getData() == null)
                {
                    return;
                }

                MeData meData = userDataResponse.getData().getMe();
                if(meData==null)
                {
                    return;
                }

                Log.d(TAG, "The userName is "+userDataResponse.getData().getMe().getDisplayName());

                if(meData.getBitmojiData()!=null)
                {
                    Glide.with(SnapLoginAct.this)
                            .load(meData.getBitmojiData().getAvatar())
                            .into(imgView);
                }
            }

            @Override
            public void onFailure(boolean b, int i) {

            }
        });
    }
}
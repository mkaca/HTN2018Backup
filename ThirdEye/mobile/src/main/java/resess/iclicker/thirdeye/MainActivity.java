package resess.iclicker.thirdeye;

import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.snapchat.kit.sdk.SnapLogin;


public class MainActivity extends Fragment {

    private View view;
    public static final String TAG = "MainActivity";

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container,
                             @Nullable Bundle savedInstanceState) {

        if(view == null)
        {
            view = inflater.inflate(R.layout.activity_main, container, false);
        }

        View loginButton = SnapLogin.getButton(getContext(), (ViewGroup)view);

        return super.onCreateView(inflater, container, savedInstanceState);
    }
}
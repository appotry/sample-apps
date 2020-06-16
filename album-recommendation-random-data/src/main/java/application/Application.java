package application;

import json.Album;
import org.apache.http.client.methods.HttpGet;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.atomic.AtomicInteger;

public class Application implements Runnable {
    RandomAlbumGenerator albumGenerator;
    BlockingQueue<Album> queue;
    VespaDataFeeder dataFeeder;
    VespaQueryFeeder queryFeeder;
    private double pushProbability = 0.05;
    private double queryProbability = 0.05;
    private final int runsPerSecond = 100;
    private boolean isGrowing = true;
    private final Random random = new Random();
    private final AtomicInteger pendingQueryRequests;

    Application() {
        albumGenerator = new RandomAlbumGenerator();
        queue = new LinkedBlockingQueue<>();
        dataFeeder = new VespaDataFeeder(queue);
        dataFeeder.start();
        pendingQueryRequests = new AtomicInteger(0);
        queryFeeder = new VespaQueryFeeder(true, pendingQueryRequests);
        queryFeeder.start();
    }

    private void updatePushProbability() {
        pushProbability += isGrowing ? random.nextDouble() * 0.1 : - random.nextDouble() * 0.1;
        if(pushProbability >= 0.95) {
            pushProbability = 0.95;
            isGrowing = false;
        } else if (pushProbability <= 0.05) {
            pushProbability = 0.05;
            isGrowing = true;
        }
    }

    private void updateQueryProbability() {
        queryProbability = (random.nextDouble() * 0.4) + 0.4;
    }

    private boolean shouldPush() {
        return random.nextDouble() < pushProbability;
    }

    private boolean shouldQuery() {
        return random.nextDouble() < queryProbability;
    }

    public void run() {
        if (shouldPush()) queue.add(albumGenerator.getRandomAlbum());
        if (shouldQuery()) pendingQueryRequests.incrementAndGet();
    }

    public static void main(String[] args) {
        int attempts = 0;
        boolean success = false;

        while (!success) {
            try {
                success = ((HttpURLConnection) new URL("http://vespa:8080/ApplicationStatus").openConnection()).getResponseCode() == 200;
            } catch (IOException ignored) {
            }
            System.out.println("Unable to connect to vespa, trying again in 20 seconds");
            attempts++;
            if (attempts >= 15) {
                System.out.println("Failure. Cannot establish connection");
                System.exit(1);
            }
            try {
                Thread.sleep(20000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        Timer timer = new Timer();
        Application app = new Application();

        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                app.run();
            }
        },
                0,
                (long) (1000.0 / (double) app.runsPerSecond));

        new Timer().scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                app.updatePushProbability();
                app.updateQueryProbability();
            }
        },
                0,
                10 * 1000);
    }
}


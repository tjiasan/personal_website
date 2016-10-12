package test;

import java.net.URL;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;

public class HeadlessSession {
      public static void main(String args[]) throws InterruptedException, Exception {
          HeadlessSession.HeadlessSessionId();
      }

      public static void HeadlessSessionId() throws Exception {
               DesiredCapabilities capabilities = new DesiredCapabilities();
           capabilities.setBrowserName("chrome");
           WebDriver driver = new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"), capabilities);
          try {
                String baseUrl = "http://www.google.com";
                driver.manage().timeouts().implicitlyWait(60, TimeUnit.SECONDS);
                driver.get(baseUrl);
                System.out.println("Title : " + driver.getTitle());
                String browserName = capabilities.getBrowserName().toLowerCase();
                System.out.println("Browser : " + browserName);
          } catch (Exception e) {
              System.out.println(e.getMessage());
          }
          finally {
            driver.close();
            driver.quit();
          }
      }
}
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.JavascriptExecutor;

public class ButtonClickAndScrollExample {
    public static void main(String[] args) {
        // Podešavanje putanje do Chrome drajvera
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\User\\Downloads\\chromedriver.exe");

        // Inicijalizacija WebDriver-a (ChromeDriver) i otvaranje veb stranice
        WebDriver driver = new ChromeDriver();
        driver.get("http://demo.baasic.com/angular/starterkit-photo-gallery/main");

        // Poziv metode koja simulira klik na dugme i scroll stranice
        clickButtonAndScroll(driver, "svg", "Display photos", "scroll__icon");

        // Zatvaranje pregledača
        driver.quit();
    }

    public static void clickButtonAndScroll(WebDriver driver, String tagName, String titleValue, String classValue) {
        // Pronalaženje elementa na osnovu kombinacije selektora
        WebElement element = driver.findElement(By.cssSelector(tagName + "[title='" + titleValue + "'][class='" + classValue + "']"));

        // Simulacija klika na dugme
        element.click();

        // Simulacija scroll-a stranice prema dole
        JavascriptExecutor jsExecutor = (JavascriptExecutor) driver;
        jsExecutor.executeScript("window.scrollBy(0, 500);");

        // Simulacija scroll-a stranice prema gore
        jsExecutor.executeScript("window.scrollBy(0, -500);");
    }
}

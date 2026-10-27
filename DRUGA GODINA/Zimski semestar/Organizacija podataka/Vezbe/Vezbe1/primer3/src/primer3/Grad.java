
package primer3;

import com.opencsv.bean.CsvBindByName;

public class Grad {

    @CsvBindByName(column = "drzava", required = true)
    private String drzava;

    @CsvBindByName(column = "grad", required = true)
    private String grad;

    public Grad() { }

    public Grad(String drzava, String grad) {
        this.drzava = drzava;
        this.grad = grad;
    }

    public String getDrzava() {
        return drzava;
    }

    public void setDrzava(String drzava) {
        this.drzava = drzava;
    }

    public String getGrad() {
        return grad;
    }

    public void setGrad(String grad) {
        this.grad = grad;
    }
}
